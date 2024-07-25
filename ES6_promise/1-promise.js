export default function getFullResponseFromAPI(success) {
    let keep = new Promise((resolve, reject) => {
      if (success === "true") {
        resolve({ status: 200, body: 'Success' });
      }
      else reject(new Error("The fake API is not working currently"));
    });
}