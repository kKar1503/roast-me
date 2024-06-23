import React from "react";

export interface EmojiRainProps {
  emojis: string[];
}

export default function EmojiRain({ emojis }: EmojiRainProps) {
  const order = [1, 6, 9, 8, 7, 0, 3, 2, 4, 5];

  return (
    <div className="FallingEmojis">
      {emojis.map((emojiElement, i) => {
        return (
          <span key={i} className={`emoji emojiAnimation${i}`}>
            {emojiElement}
          </span>
        );
      })}
    </div>
  );
}
