import * as c from "./components/componentsIndex";

function App() {

  return (
    <section className="layout">
      <c.Skeleton
        loading={false}
      >
        <c.Container
          boxShadow="0px 4px 8px 0px rgba(0,0,0,0.5)"
          padding={"3rem"}
          flexDirection="column"
          borderRadius={8}
          gap={"1rem"}
        >
          <c.TextInput
            onChange={() => {}}
          />
          <c.TextInput
            onChange={() => {}}
          />
        </c.Container>
      </c.Skeleton>
    </section>
  )
}

export default App
