import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signup = signUpUser(firstName, lastName);
  const photo = uploadPhoto(fileName);

  return Promise.allSettled([signup, photo]).then((results) =>
    results.map((res) => {
      if (res.status === 'fulfilled') {
        return {
          status: res.status,
          value: res.value,
        };
      }
      return {
        status: res.status,
        value: res.reason.toString(), // Convert Error → string
      };
    })
  );
}
