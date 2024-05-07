<template>
  <div class="min-h-screen flex items-center justify-center bg-cover bg-center" style="background-image: url('https://i0.wp.com/metrology.news/wp-content/uploads/2022/02/Autodesk-Acquisitions-Enable-Commitment-To-Providing-Full-Gamut-of-Smart-Manufacturing-Solutions.png?resize=800%2C445&ssl=1');">
    <div class="max-w-md w-full bg-deep-cerulean-200 bg-opacity-75 shadow-md rounded-md p-8 text-white">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-white-900">
          Sign in to your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="login">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">Username</label>
            <input
              id="username"
              v-model="username"
              name="username"
              type="text"
              autocomplete="username"
              required
              class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Username"
            >
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm mt-4"
              placeholder="Password"
            >
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              class="h-4 w-4 text-deep-cerulean-700 focus:ring-deep-cerulean-800 border-gray-300 rounded"
            >
            <label for="remember-me" class="ml-2 block text-sm text-white-900">
              Remember me
            </label>
          </div>

          <div class="text-sm">
            <a href="#" class="font-medium text-deep-cerulean-600 hover:text-deep-cerulean-500">
              Forgot your password?
            </a>
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="isLoggingIn"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-deep-cerulean-600 hover:bg-deep-cerulean-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-deep-cerulean-500 mt-4"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg
                class="h-5 w-5 text-deep-cerulean-500 group-hover:text-deep-cerulean-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M3.293 7.293a1 1 0 011.414-1.414L9 10.586l4.293-4.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5z"
                  clip-rule="evenodd"
                />
              </svg>
            </span>
            Sign in
          </button>
        </div>

        <div class="mt-6 flex justify-center items-center">
          <button @click="toggleRegister" class="text-sm text-deep-cerulean-800 hover:text-deep-cerulean-500">
            Don't have an account? Register here
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../store';
import { useRouter } from 'vue-router';
import Toastify from 'toastify-js';
import bcrypt from 'bcryptjs'; // Import bcryptjs library

let username = ref('');
let password = ref('');
let isLoggingIn = ref(false);
const store = useAuthStore();
const router = useRouter();

const toggleRegister = () => {
  router.push('/user/register');
};

const login = () => {
  isLoggingIn.value = true;
  
  // Hash the password
  const hashedPassword = bcrypt.hashSync(password.value, 10); // Hash the password

  const userData = {
    username: username.value,
    password: hashedPassword // Send hashed password to backend
  };

  fetch('http://172.18.101.47:1234/SMW/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    isLoggingIn.value = false;
    if (data.access_token) {
      store.login(username.value, hashedPassword); // Send hashed password to the store
      if (data.is_admin) {
        router.push('/admindashboard');
      } else {
        router.push('/publicdashboard');
      }
      Toastify({
        text: data.message,
        duration: 3000,
        newWindow: true,
        close: true,
        gravity: "bottom", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        backgroundColor: "green",
      }).showToast();
    } else {
      Toastify({
        text: data.detail[0].msg,
        backgroundColor: "linear-gradient(to right, #ff416c, #ff4b2b)",
      }).showToast();
    }
  })
  .catch((error) => {
    console.error('Error:', error);
    isLoggingIn.value = false;
    Toastify({
      text: 'An error occurred. Please try again later.',
      backgroundColor: "linear-gradient(to right, #f44336, #d32f2f)",
    }).showToast();
  });
}


</script>

<style>
/* Add your component's style here */
</style>
