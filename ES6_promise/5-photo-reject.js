export default function uploadPhoto(filename) {
  const myPromise = new Promise((reject) => {
    reject(filename);
  });

  return myPromise.catch((file) => `Error: ${file} cannot be processed`);
}
