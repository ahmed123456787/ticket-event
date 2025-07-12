const Work = () => {
  return (
    <div className="flex flex-col mt-12 px-6 md:px-12">
      <h2 className="text-[var(--bgDarkBlueColor)] text-center text-4xl md:text-7xl mx-4 md:mx-72 font-bold leading-snug">
        Keep more of your money with the{" "}
        <span className="bg-[#FFEAAE] rounded-3xl px-2 py-1">lowest fees </span>
        available on the market.
      </h2>

      <div className="flex flex-col md:flex-row mt-12">
        {/* Left Section: Steps Image */}
        <div className="w-full md:w-1/2 mb-6 md:mb-0">
          <img src="/work.png" alt="Steps" className="w-full h-auto" />
        </div>

        {/* Right Section: Description */}
        <div className="w-full md:w-1/2 md:pl-12">
          <h3 className="text-[var(--bgDarkBlueColor)] text-2xl md:text-3xl font-bold mb-4">
            Incredible events at your fingertips
          </h3>
          <p className="text-gray-600 mb-6 text-sm md:text-base">
            Created for technophobes and developers alike, Ticket Tailor is the
            platform for hassle-free event management. Start selling tickets in
            minutes with just a few simple steps.
          </p>
          <ul className="list-none space-y-2 text-sm md:text-base">
            <li className="flex items-center">
              <span className="text-green-500 mr-2">✔</span>
              Create your box office and get started for free
            </li>
            <li className="flex items-center">
              <span className="text-green-500 mr-2">✔</span>
              Customise 'til your heart's content
            </li>
            <li className="flex items-center">
              <span className="text-green-500 mr-2">✔</span>
              Get going without a website (we're self-hosted)
            </li>
          </ul>
          <div className="mt-6 flex flex-col md:flex-row">
            <input
              type="email"
              placeholder="Enter email *"
              className="border rounded-lg p-3 flex-grow mb-4 md:mb-0 md:rounded-l-lg"
            />
            <button className="bg-[var(--bgDarkBlueColor)] text-white px-6 py-3 rounded-lg md:rounded-r-lg">
              Get started
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Work;
