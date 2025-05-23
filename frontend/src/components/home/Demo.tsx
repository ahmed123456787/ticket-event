import { useState } from "react";
import { Star } from "lucide-react";

const Demo = () => {
  const [email, setEmail] = useState("");

  const leftImages = ["/event-1.jpg", "/event-2.jpeg", "/event-3.jpg"];
  const rightImages = ["/event-4.jpeg", "/event5.png", "/event-6.jpg"];

  const companyReviews = [
    { name: "Google", rating: 5 },
    { name: "Microsoft", rating: 5 },
    { name: "Amazon", rating: 4 },
  ];

  return (
    <div className="bg-[var(--bgBeigeColor)] flex items-center justify-center ">
      <div className="w-full grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 max-w-7xl mx-auto">
        <div className="flex flex-col justify-center">
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold mb-2 md:mb-4 leading-tight">
            The world's most loved ticketing platform
          </h2>
          <p className="text-base sm:text-lg mt-2  text-gray-700 max-w-xl">
            Whether it's your first event ever, or your biggest event yet, we
            make it simple and affordable to sell tickets online.
          </p>
          <form className="flex flex-col sm:flex-row items-start sm:items-center gap-4 sm:gap-2 w-full max-w-xl">
            <div className="relative flex-grow w-full">
              <input
                type="email"
                value={email}
                required
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
                className="w-full px-4 py-3 rounded-xl sm:rounded-l-xl sm:rounded-r-none border border-gray-300 "
              />
              <button
                type="submit"
                className="w-full sm:w-auto mt-2 sm:mt-0 sm:absolute sm:right-0 sm:top-0 sm:h-full text-white px-6 py-3 sm:py-2 rounded-xl  bg-[var(--bgDarkBlueColor)] "
              >
                Get Started
              </button>
            </div>
            <button className="text-sm font-semibold">Book a demo</button>
          </form>

          {/* Company reviews section */}
          <div className="mt-6">
            <p className="text-lg font-semibold mb-3">
              Trusted by leading companies
            </p>
            <div className="flex flex-wrap gap-6">
              {companyReviews.map((review) => (
                <div key={review.name} className="flex flex-col">
                  <div className="flex items-center">
                    {[...Array(review.rating)].map((_, i) => (
                      <Star
                        key={`${review.name}-${i}`}
                        className="text-amber-300 fill-amber-300 w-5 h-5"
                      />
                    ))}
                    {review.rating < 5 &&
                      [...Array(5 - review.rating)].map((_, i) => (
                        <Star
                          key={`${review.name}-empty-${i}`}
                          className="text-amber-300 w-5 h-5"
                        />
                      ))}
                  </div>
                  <p className="text-sm font-medium mt-1 text-gray-700">
                    {review.name}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right side - Moving images */}
        <div className="hidden md:flex gap-4 h-[500px] lg:h-[600px] overflow-hidden relative image-container">
          {/* Left column */}
          <div className="flex-1 animate-slideUp">
            <div className="flex flex-col gap-4">
              {[...leftImages, ...leftImages].map((src, index) => (
                <img
                  key={`left-${index}`}
                  src={src}
                  alt={`Event ${index + 1}`}
                  className="w-full h-48 object-cover rounded-lg shadow-md"
                />
              ))}
            </div>
          </div>
          {/* Right column - Delayed animation */}
          <div className="flex-1 animate-slideUp animation-delay-1000">
            <div className="flex flex-col gap-4">
              {[...rightImages, ...rightImages].map((src, index) => (
                <img
                  key={`right-${index}`}
                  src={src}
                  alt={`Event ${index + 4}`}
                  className="w-full h-48 object-cover rounded-lg shadow-md"
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Demo;
