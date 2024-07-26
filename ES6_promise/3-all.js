import { uploadPhoto, createUser } from "./utils";

export default function handleProfileSignup() {
    let myPromise = Promise.all([uploadPhoto(), createUser()]).then(
        ([result1, result2]) => {
            let myBody = result1.body;
            let myName = result2.firstName;
            let myLast = result2.lastName;

            console.log(`${myBody} ${myName} ${myLast}`);
        }
    ).catch(() => {
        console.log("Signup system offline");
    });

    return myPromise;
} 