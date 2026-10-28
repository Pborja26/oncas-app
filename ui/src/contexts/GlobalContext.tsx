import React, {
  createContext
} from "react";

interface IGlobalContext {
  
};

export const GlobalContext = createContext<IGlobalContext>({} as IGlobalContext);

export const GlobalProvider: React.FC<{
  children: React.ReactNode;
}> = ({ children }) => {

  const values = {

  };

  return (
    <GlobalContext.Provider
      value={values}
    >
      {children}
    </GlobalContext.Provider>
  )
}