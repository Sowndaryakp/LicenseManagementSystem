<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Register
          </h2>
        </div>
        <form class="mt-8 space-y-6" @submit.prevent="register">
          <div class="rounded-md shadow-sm -space-y-px">
            <div>
              <label for="email-address" class="sr-only">Email address</label>
              <input
                id="email-address"
                v-model="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Email address"
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
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Password"
              >
            </div>
            <div>
              <label for="company" class="sr-only">Company</label>
              <input
                id="company"
                v-model="company"
                name="company"
                type="text"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Company"
              >
            </div>
            <div>
              <label for="username" class="sr-only">Username</label>
              <input
                id="username"
                v-model="username"
                name="username"
                type="text"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Username"
              >
            </div>
          </div>
  
          <div>
            <button
              type="submit"
              :disabled="isRegistering"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                <svg
                  class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
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
              Register
            </button>
          </div>
  
          <div class="mt-6 flex justify-center items-center">
            <button @click="toggleLogin()" class="text-sm text-indigo-600 hover:text-indigo-500">
              Back to Login
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
  
  const router = useRouter();
  let email = ref('');
  let password = ref('');
  let company = ref('');
  let username = ref('');
  let isRegistering = ref(false);
  const store = useAuthStore();
  const toggleLogin=() => {
    router.push('/user/login');
  };
  const register = () => {
    isRegistering.value = true;
    console.log("Email:", email.value);
    console.log("Password:", password.value);
    console.log("Company:", company.value);
    console.log("Username:", username.value);
    // Simulating registration process, you can use your registration logic here.
    // Once registered, redirect the user to login page.
    setTimeout(() => {
      isRegistering.value = false;
      showRegistrationForm.value = false;
      Toastify({
        text: 'Registered Successfully! Please login to continue.',
        backgroundColor: "linear-gradient(to right, #4caf50, #56ab2f)",
      }).showToast();
    }, 1000);
  }
  </script>
  
  <style>
  /* Add your component's style here */
  </style>
  