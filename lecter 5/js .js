alert("Hello, World!");
let user = {
    name: "John",
    age: 330,
    email: "john@example.com",
    number: 1234567890,
    address: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        zip: "12345₹₹",
    },
    subject: "Math",
    isenrolled: true,
    graduationyear: 2022,
};
console.log(user.name);
console.log(user.age);
console.log(user.email);
console.log(user.number);
console.log(user.address.street);
console.log(user.address.city);
console.log(user.subject);
console.log(user.isenrolled);
console.log(user);
console.log(
    user.name +
        " is " +
        user.age +
        " years old and lives at " +
        user.address.street +
        ", " +
        user.address.city +
        ", " +
        user.address.state +
        " " +
        user.address.zip +
        ". He is enrolled in " +
        user.subject +
        ".",
);
console.log(
    `User ${user.name} is ${user.age} years old and lives at ${user.address.street}, ${user.address.city}, ${user.address.state} ${user.address.zip}. He is enrolled in ${user.subject}.`,
);
delete user.name;
user.name = "Jane";
user.age = 25;
console.log(user);

