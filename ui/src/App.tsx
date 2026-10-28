import { useEffect, useState } from 'react';
import { auth } from './services/auth';
import type { User } from './services/auth';

function App() {
  const [user, setUser] = useState<User | null>(null);
  const [login, setLogin] = useState<{ username: string, password: string }>({
    username: "",
    password: ""
  });

  useEffect(() => {
    const autoLogin = async () => {
      await auth.csrf();
      try {
        const { status, data } = await auth.user();
        setUser(data);
      } catch {
        setUser(null);
      }
    };
    autoLogin();
  }, []);

  return (
    <section className="layout">
      <input 
        onChange={(e) => setLogin((prev) => ({...prev, username: e.target.value}))}
        className="input"
      />
      <input 
        onChange={(e) => setLogin((prev) => ({...prev, password: e.target.value}))}
        className="input"
        type='password'
      />
      <button
        onClick={() => auth.login(login.username, login.password)}
        className="btn"
      >
        Login
      </button>
      <button
        onClick={() => auth.logout()}
        className="btn"
      >
        Logout
      </button>
    </section>
  )
}

export default App
