import styled from "styled-components";
import type { ITextInputProps } from "./textInput.types";

type InputStyleProps = Omit<ITextInputProps, "onChange">;

export const Input = styled.input<InputStyleProps>`
  /* flex: 1; */
  padding: 8px 16px;
  border: 1px solid ${(props) => props.disabled ? "#C0C0C0" : "#2a16e1" };
  border-radius: 16px;
`;