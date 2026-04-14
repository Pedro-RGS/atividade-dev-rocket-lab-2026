import { Link } from "react-router-dom";
import { CustomLogo } from "../atoms/custom-logo"
import { SearchBar } from "../molecules/search-bar";
import { CustomIcon } from "../atoms/custom-icon";
import { ShoppingCart, User } from "lucide-react";
import logoSvg from "../../assets/logo.svg"

interface HeaderProps {
  onSearch?: (query: string) => void;
}

export const Header = ({ onSearch }: HeaderProps) => {

  const handleSearch = (query: string) => {
    if (onSearch) {
      onSearch(query);
    }
  };


  return (
    <header className="w-full bg-black border-b border-zinc-900 sticky top-0 z-50">
      <div className="container mx-auto px-4 h-20 flex items-center justify-between gap-8">
        <Link to="/" className="shrink-0">
          <CustomLogo src={logoSvg} alt="Lojas H1gH" size="md" />
        </Link>

        <div className="flex-1 max-w-2xl hidden md:block">
          <SearchBar onSearch={handleSearch} placeholder="Buscar produtos..." />
        </div>

        <div>
          <button className="relative p-2 hover:bg-gray-50 rounded-full transition-colors">
            <CustomIcon icon={User} size="md" color="primary" />
          </button>
          <button className="relative p-2 hover:bg-gray-50 rounded-full transition-colors">
            <CustomIcon icon={ShoppingCart} size="md" color="primary" />
            <span className="absolute top-0 right-0 bg-(--color-primary) text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full">
              3
            </span>
          </button>
        </div>

        <div className="md:hidden px-4 pb-4">
          <SearchBar onSearch={handleSearch} />
        </div>
      </div>
    </header>
  );
};
