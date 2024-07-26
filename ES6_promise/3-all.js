import { uploadPhoto, createUser } from "./ES6_promise/utils";

export default function handleProfileSignup() {
    let myPromise = Promise.all([uploadPhoto(), createUser()]).then(
        (result1, result2) => {
            let myBody = result1.status;
            let myName = result2.firstName;
            let myLast = result2.lastName;

            console.log(`${myBody} ${myName} ${myLast}`);
        }
    ).catch((error) => {
        console.log("Signup system offline");
    });

    return myPromise;
} 