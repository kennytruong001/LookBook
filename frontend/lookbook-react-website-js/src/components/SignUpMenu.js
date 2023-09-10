import React from 'react'

function SignUpMenu() {
  return (
    <form method="POST">
        <link
            rel="stylesheet"
            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
            crossorigin="anonymous"
        />
        <link
            rel="stylesheet"
            href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
            crossorigin="anonymous"
        />
        <select name="class_type" id="class_type">
            <option value="user">User</option>
            <option value="customer">Customer</option>
        </select>
        <div class="form-group">
            <label for="email">Email Address</label>
            <input
            type="email"
            class="form-control"
            id="email"
            name="email"
            placeholder="Enter email"
            />
        </div>
        <div class="form-group">
            <label for="firstName">First Name</label>
            <input
            type="text"
            class="form-control"
            id="firstName"
            name="firstName"
            placeholder="Enter first name"
            />
        </div>
        <div class="form-group">
            <label for="lastName">Last Name</label>
            <input
            type="text"
            class="form-control"
            id="lastName"
            name="lastName"
            placeholder="Enter last name"
            />
        </div>
        <div class="form-group">
            <label for="password1">Password</label>
            <input
            type="password"
            class="form-control"
            id="password1"
            name="password1"
            placeholder="Enter password"
            />
        </div>
        <div class="form-group">
            <label for="password2">Password (Confirm)</label>
            <input
            type="password"
            class="form-control"
            id="password2"
            name="password2"
            placeholder="Confirm password"
            />
        </div>
        <br />
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  );
}

export default SignUpMenu