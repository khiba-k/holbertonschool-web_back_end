import { createClient } from "redis";

const subscriber = createClient();

subscriber.on("connect", () => {
  console.log("Redis client connected to the server");
});

subscriber.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
subscriber.subscribe("holberton school channel");

// Handle incoming messages
subscriber.on("message", (channel, message) => {
  console.log(message);

  if (message === "KILL_SERVER") {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
