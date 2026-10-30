import { SkeletonBlock, SkeletonWrapper } from "./skeleton.style";
import type { CSSProperties, ReactNode } from "react";

interface ISkeleton {
  count?: number;
  loading?: boolean;
  children?: ReactNode;
  width?: CSSProperties["width"];
  height?: CSSProperties["height"];
  borderRadius?: CSSProperties["borderRadius"];
};

const toCssSize = (value?: string | number) =>
  typeof value === "number" ? `${value}px` : value;

const Skeleton = ({
  count = 1,
  loading = true,
  children,
  ...props
}: ISkeleton) => {
  const width = toCssSize(props.width);
  const height = toCssSize(props.height);
  const borderRadius = toCssSize(props.borderRadius);

  if (children) {
    if (!loading) return <>{children}</>;

    return (
      <SkeletonWrapper $width={width} $borderRadius={borderRadius} aria-busy="true">
        <div aria-hidden="true" inert>{children}</div>
      </SkeletonWrapper>
    );
  }

  return (
    <>
      {Array.from({ length: count }).map((_, index) => (
        <SkeletonBlock
          key={`skeleton-${index}`}
          $width={width}
          $height={height}
          $borderRadius={borderRadius}
        />
      ))}
    </>
  );
};

export default Skeleton;
