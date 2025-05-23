import { Menu, Search, X } from "lucide-react";
import { useState } from "react";

interface NavItemProps {
  text: string;
  onClick?: () => void;
}

const NavItem = ({ text, onClick }: NavItemProps) => (
  <h2
    onClick={onClick}
    className="text-[var(--bgDarkBlueColor)] hover:border-b-2 hover:border-[var(--bgDarkBlueColor)] pb-1 transition-all cursor-pointer"
  >
    {text}
  </h2>
);

const TopBar = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navItems = ["how it works?", "Features", "Pricing", "About us"];

  return (
    <div className="w-full flex flex-col bg-[color:var(--bgDarkBlueColor)]">
      <p className="text-white text-center text-sm md:text-md p-2">
        Create your events with our magic tool !!
      </p>
      <div className="flex items-center justify-between bg-white px-4 md:px-12">
        <div className="flex-none">
          <img
            src="logo.png"
            alt="logo"
            className="w-20 h-20 md:w-32 md:h-32"
          />
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex flex-1 justify-center gap-8 text-sm">
          {navItems.map((item) => (
            <NavItem key={item} text={item} />
          ))}
        </nav>

        {/* Desktop Buttons */}
        <div className="hidden md:flex flex-none items-center gap-4 font-bold">
          <button className="px-4 py-2 hover:bg-[var(--bgBeigeHoverColor)] hover:rounded-xl transition-transform hover:scale-110">
            Login
          </button>
          <button className="text-white px-4 py-2 rounded-3xl bg-[var(--bgDarkBlueColor)] transition-transform hover:scale-110">
            Get Started
          </button>
          <Search className="w-6 h-6" />
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden p-2"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="absolute top-[88px] left-0 right-0 bg-[color:var(--bgBeigeColor)] p-4 z-50 border-t md:hidden">
            <nav className="flex flex-col gap-4">
              {navItems.map((item) => (
                <NavItem
                  key={item}
                  text={item}
                  onClick={() => setMobileMenuOpen(false)}
                />
              ))}
              <div className="flex flex-col gap-2 pt-4 border-t">
                <button className="w-full px-4 py-2 text-center hover:bg-[var(--bgBeigeHoverColor)] rounded-xl transition-all">
                  Login
                </button>
                <button className="w-full text-white px-4 py-2 rounded-xl bg-[var(--bgDarkBlueColor)] transition-all">
                  Get Started
                </button>
              </div>
            </nav>
          </div>
        )}
      </div>
    </div>
  );
};

export default TopBar;
