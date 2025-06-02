import TopBar from "../components/dashboard/TopBar";
import Sidebar from "../components/dashboard/Sidebar";

const MainLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex flex-col h-screen">
      <TopBar />
      <div className="flex flex-1 overflow-hidden">
        <div className=" flex-shrink-0">
          <Sidebar />
        </div>
        <main className="flex-1  sm:px-0 md:px-24 mt-12 overflow-y-auto ">
          {children}
        </main>
      </div>
    </div>
  );
};

export default MainLayout;

<svg viewBox="0 0 144 144"><g fill="none" fill-rule="evenodd"><g><path fill="#D65129" fill-rule="nonzero" d="M25.5 61.5h93v51h-93z"></path><path fill="#D65129" fill-rule="nonzero" d="M72 87l-46.5 25.5v-51z"></path><path fill="#F16932" fill-rule="nonzero" d="M103.5 69.75v42.75h15v-51zM25.5 112.5h78V69.75z"></path><path fill="#3A3A3A" fill-rule="nonzero" d="M120 114H24V60h15v3H27v48h90V63h-12v-3h15z"></path><path fill="#FFF" fill-rule="nonzero" d="M103.5 70.5L72 87 40.5 70.5v-39h51l12 12z"></path><path d="M72 87.9L39.75 70.95v-40.2H91.8l12.45 12.45v27.75L72 87.9zM41.25 70.05L72 86.1l30.75-16.05V43.8L91.2 32.25H41.25v37.8z" fill="#3A3A3A" fill-rule="nonzero"></path><path fill="#3A3A3A" fill-rule="nonzero" d="M24.706 111.18l92.985-50.999 1.442 2.63-92.984 51z"></path><path fill="#3A3A3A" fill-rule="nonzero" d="M24.75 62.797l1.442-2.63 46.558 25.53-1.442 2.631zM103.5 45H90V31.5h3V42h10.5z"></path><path fill="#3A3A3A" fill-rule="nonzero" d="M105 70.5h-3V44.1L90.9 33H42v37.5h-3V30h53.1L105 42.9z"></path><path fill="#3A3A3A" fill-rule="nonzero" d="M68.1 55.05H93v3H68.1zM68.1 61.35h16.05v3H68.1zM68.1 48.45h16.05v3H68.1zM42.75 17.25h3v6h-3zM26.25 33.75h6v3h-6zM29.386 23.258l2.12-2.122 3.607 3.607-2.121 2.121z"></path><path fill="#D65129" fill-rule="nonzero" d="M61.5 65.7l-6-6-6 6V43.2h12z"></path><circle fill="#F16932" fill-rule="nonzero" cx="55.5" cy="45.45" r="9"></circle><path d="M0 0h144v144H0z"></path></g></g></svg>
