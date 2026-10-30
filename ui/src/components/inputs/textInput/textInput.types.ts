import type { CSSProperties } from "react";

export interface ITextInputProps extends CSSProperties {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  disabled?: boolean;
  error?: boolean;
  password?: boolean;
  placeholder?: string;
}