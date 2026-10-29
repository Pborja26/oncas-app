from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from utils.models import Theme, ThemeCategorie

User = get_user_model()

# Usuários de teste para o filtro created_by / updated_by por nome.
# Senha inutilizável: servem apenas como autores dos registros.
USERS = [
    {"username": "seed_maria", "first_name": "Maria", "last_name": "Silva"},
    {"username": "seed_joao", "first_name": "João", "last_name": "Souza"},
]

# categoria -> (descrição, ativo, autor, [(nome, cor, ativo)])
THEMES = {
    "primary": ("Cores principais da marca", True, "seed_maria", [
        ("50", "#fffbeb", True),
        ("300", "#fcd34d", True),
        ("500", "#f59e0b", True),
        ("700", "#b45309", True),
        ("900", "#78350f", False),
    ]),
    "secondary": ("Cores de apoio", True, "seed_joao", [
        ("300", "#93c5fd", True),
        ("500", "#3b82f6", True),
        ("900", "#1e3a8a", True),
    ]),
    "neutral": ("Fundos, bordas e textos", True, "seed_maria", [
        ("100", "#f3f4f6", True),
        ("300", "#d1d5db", True),
        ("500", "#6b7280", True),
        ("800", "#1f2937", True),
    ]),
    "feedback": ("Estados de sucesso, alerta e erro", True, "seed_joao", [
        ("success", "#22c55e", True),
        ("warning", "#eab308", True),
        ("error", "#ef4444", True),
        ("info", "#0ea5e9", False),
    ]),
    "legacy": ("Paleta antiga, desativada", False, "admin", [
        ("main", "#7c3aed", False),
        ("accent", "#db2777", False),
    ]),
}


class Command(BaseCommand):
    help = "Popula categorias e cores de theme para testes locais (idempotente)."

    @transaction.atomic
    def handle(self, *args, **options):
        users = {}
        for data in USERS:
            user, created = User.objects.get_or_create(
                username=data["username"],
                defaults={"first_name": data["first_name"], "last_name": data["last_name"]},
            )
            if created:
                user.set_unusable_password()
                user.save()
            users[user.username] = user

        admin = User.objects.filter(is_superuser=True).order_by("id").first()
        if admin is None:
            self.stderr.write("Nenhum superuser encontrado. Rode createsuperuser antes.")
            return
        users["admin"] = admin

        for category_name, (description, active, author, colors) in THEMES.items():
            category, _ = ThemeCategorie.objects.update_or_create(
                name=category_name,
                defaults={
                    "description": description,
                    "active": active,
                    "created_by": users[author],
                    "updated_by": users[author],
                },
            )
            for name, color, color_active in colors:
                # Alterna o updated_by para ter casos em que difere do created_by
                editor = users["admin"] if name in ("500", "error") else users[author]
                Theme.objects.update_or_create(
                    color=color,
                    defaults={
                        "name": name,
                        "category": category,
                        "active": color_active,
                        "created_by": users[author],
                        "updated_by": editor,
                    },
                )

        self.stdout.write(self.style.SUCCESS(
            f"{ThemeCategorie.objects.count()} categorias, {Theme.objects.count()} cores."
        ))
