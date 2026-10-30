import type { CSSProperties } from "react";

interface IContainer extends CSSProperties {
  children: React.ReactNode;
};

const Container = ({
  children,
  ...props
}: IContainer) => {
  return (
    <div
      style={{ 
        display: "flex",
        ...props 
      }}
    >
      {children}
    </div>
  );
};

export default Container;
