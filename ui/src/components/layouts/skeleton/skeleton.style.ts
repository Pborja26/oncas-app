import styled, { css, keyframes } from "styled-components";

const shimmer = keyframes`
  0% { background-position: 200% 0; }
  100% {background-position: -200% 0; }
`;

const shimmerBackground = css`
  background: linear-gradient(90deg, #e0e0e0 25%, #f0f0f0 50%, #e0e0e0 75%);
  background-size: 200% 100%;
  animation: ${shimmer} 1.4s ease-in-out infinite;
`;

interface ISkeletonStyle {
  $width?: string;
  $height?: string;
  $borderRadius?: string;
};

export const SkeletonBlock = styled.div<ISkeletonStyle>`
  display: block;
  ${shimmerBackground}
  width: ${(props) => props.$width ?? "100%"};
  height: ${(props) => props.$height ?? "100%"};
  border-radius: ${(props) => props.$borderRadius ?? "8px"};
  cursor: progress;
`;

export const SkeletonWrapper = styled.div<ISkeletonStyle>`
  position: relative;
  width: ${(props) => props.$width ?? "fit-content"};
  border-radius: ${(props) => props.$borderRadius ?? "8px"};
  overflow: hidden;
  cursor: progress;

  & > * {
    visibility: hidden;
  }

  &::after {
    content: "";
    position: absolute;
    inset: 0;
    ${shimmerBackground}
  }
`;
