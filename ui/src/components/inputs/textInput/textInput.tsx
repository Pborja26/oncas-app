import type { ITextInputProps } from "./textInput.types";
import * as s from "./textInput.styled";

const TextInput = ({
  onChange,
  placeholder,
  error,
  disabled,
  password,
  ...props
}: ITextInputProps) => {

  return (
    <s.Input
      onChange={onChange}
      placeholder={placeholder}
      error={error}
      disabled={disabled}
      type={password ? "password" : "text"}
      style={{...props}}
    />
  );
};

export default TextInput;
