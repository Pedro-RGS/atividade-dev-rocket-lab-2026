import { Route, Routes } from 'react-router-dom'
import { HomePage } from "./pages/home-page";
import { ProductPage } from "./pages/product-page"

function App() {

  return (
    <>
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/product/:id" element={<ProductPage />} />
        </Routes>
      </main>
    </>
  );
}

export default App
