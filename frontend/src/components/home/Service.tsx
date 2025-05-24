import { FC } from "react";

const Service: FC = () => {
  const services = [
    {
      title: "First-timers",
      description:
        "Easily create events and start selling tickets for free, with a range of features and helpful support 24/7 from real humans.",
      bgColor: "bg-[#FFD0C7]", // Light pink
      textColor: "text-black",
      linkText: "Learn more",
    },
    {
      title: "Event pros",
      description:
        "Level up your ticketing with powerful features and unbeatable pricing. With 99.9% uptime and 24-7 support, we'll be there at every step.",
      bgColor: "bg-white",
      textColor: "text-black",
      linkText: "Learn more",
    },
    {
      title: "Free events",
      description:
        "If your events free, so are we. Discover all the features and support you need to make your events a success.",
      bgColor: "bg-[#FFEAAE]", // Light yellow
      textColor: "text-black",
      linkText: "Learn more",
    },
    {
      title: "Developers",
      description:
        "Build the future of ticketing with our powerful API and easy-to-use integrations. Plus, 24/7 support makes set-up a breeze.",
      bgColor: "bg-[#C0DFD3]", // Light green
      textColor: "text-black",
      linkText: "Learn more",
    },
    {
      title: "Charities",
      description:
        "From town hall jumble sales to grand annual fundraisers, charities get 50% off our fees and all the features you need.",
      bgColor: "bg-[#FFA69E]", // Coral
      textColor: "text-black",
      linkText: "Learn more",
    },
    {
      title: "Attractions",
      description:
        "With extensive time slot management and our (free) check-in app, we work with national museums, festive lightshows, and everything in between.",
      bgColor: "bg-white",
      textColor: "text-black",
      linkText: "Learn more",
    },
  ];

  return (
    <div className="bg-[var(--bgDarkBlueColor)] text-white py-16 px-4 sm:px-8 lg:px-16">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
          <div>
            <h2 className="text-4xl sm:text-5xl lg:text-6xl font-bold leading-tight">
              Join over{" "}
              <span className="bg-[#FFEAAE] text-[var(--bgDarkBlueColor)] px-3 py-1 rounded-lg inline-block">
                73,000 Event
              </span>{" "}
              <br />
              <span className="bg-[#FFEAAE] text-[var(--bgDarkBlueColor)] px-3 py-1 rounded-lg inline-block mb-2">
                Creators
              </span>
              across 120 <br />
              countries
            </h2>
          </div>
          <div className="flex items-center">
            <p className="text-xl">
              Whether you're running a sell-out festival in London, managing a
              lightshow in LA, or dance classes in Adelaide, we make it
              easy-peasy to sell tickets online.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((service, index) => (
            <div
              key={index}
              className={`${service.bgColor} ${service.textColor} p-6 rounded-xl shadow`}
            >
              <h3 className="text-3xl font-bold mb-3">{service.title}</h3>
              <p className="mb-6">{service.description}</p>
              <a
                href="#"
                className="font-medium border-b-2 border-black pb-1 hover:opacity-80 transition-opacity"
              >
                {service.linkText}
              </a>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Service;
