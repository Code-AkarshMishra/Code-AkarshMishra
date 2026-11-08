
"use client";

import { useEffect, useState } from "react";
import confetti from "canvas-confetti";

export default function DiwaliFireworks() {
  const [showGreeting, setShowGreeting] = useState(true);

  useEffect(() => {
    const canvas = document.createElement("canvas");

    Object.assign(canvas.style, {
      position: "fixed",
      inset: "0",
      width: "100%",
      height: "100%",
      pointerEvents: "none",
      zIndex: "9998",
    });

    document.body.appendChild(canvas);

    const fire = confetti.create(canvas, {
      resize: true,
      useWorker: false,
    });

    const colors = [
      "#FFD700", "#FF4500", "#FF1744",
      "#FF69B4", "#00FFFF", "#FFFFFF",
      "#FFA500", "#ADFF2F", "#DA70D6"
    ];

    const timers = [];

    const launchFirework = () => {
      const x = 0.08 + Math.random() * 0.84;
      const y = 0.12 + Math.random() * 0.42;

      // Rocket trail
      fire({
        particleCount: 5,
        angle: 90,
        spread: 8,
        startVelocity: 58,
        gravity: 1.1,
        ticks: 75,
        origin: { x, y: 1 },
        colors: ["#FFD700", "#FFFFFF"],
        scalar: 0.65,
      });

      // Sky explosion
      const timer = setTimeout(() => {
        fire({
          particleCount: 150,
          spread: 360,
          startVelocity: 42,
          gravity: 0.8,
          decay: 0.94,
          ticks: 200,
          origin: { x, y },
          colors,
          scalar: 1.25,
          shapes: ["circle"],
        });

        // Golden sparkling finish
        fire({
          particleCount: 55,
          spread: 360,
          startVelocity: 25,
          gravity: 0.6,
          decay: 0.95,
          ticks: 160,
          origin: { x, y },
          colors: ["#FFD700", "#FFFACD", "#FFFFFF"],
          scalar: 0.7,
        });
      }, 600);

      timers.push(timer);
    };

    // Grand opening
    launchFirework();
    launchFirework();
    launchFirework();

    const interval = setInterval(launchFirework, 550);

    const greetingTimer = setTimeout(() => {
      setShowGreeting(false);
    }, 6500);

    const stopTimer = setTimeout(() => {
      clearInterval(interval);
    }, 15000);

    return () => {
      clearInterval(interval);
      clearTimeout(greetingTimer);
      clearTimeout(stopTimer);
      timers.forEach(clearTimeout);
      fire.reset();
      canvas.remove();
    };
  }, []);

  return (
    <>
      {showGreeting && (
        <div className="fixed inset-0 z-[9999] flex items-center justify-center pointer-events-none">
          <div className="text-center px-4 animate-[diwaliAppear_1.2s_ease-out]">
            <div className="text-4xl mb-4">🪔 ✨ 🪔</div>

            <h1 className="text-4xl sm:text-6xl md:text-7xl font-black tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-amber-500 to-yellow-200 drop-shadow-[0_0_25px_rgba(255,190,0,0.8)]">
              HAPPY DIWALI
            </h1>

            <p className="mt-5 text-sm sm:text-lg font-semibold tracking-[0.25em] text-amber-400 drop-shadow-lg">
              MAY YOUR LIFE SHINE WITH HAPPINESS
            </p>

            <div className="mt-5 text-2xl">
              ✨ 🎆 🪔 🎆 ✨
            </div>
          </div>
        </div>
      )}

      <style jsx global>{`
        @keyframes diwaliAppear {
          0% {
            opacity: 0;
            transform: scale(0.65);
          }
          70% {
            opacity: 1;
            transform: scale(1.08);
          }
          100% {
            opacity: 1;
            transform: scale(1);
          }
        }
      `}</style>
    </>
  );
}
