<template>
    <nav class="bg-gray-800 p-4 flex justify-between items-center">
        <div class="flex items-center">
      <img src="../assets/cmti.png" alt="Logo" class="h-8 mr-2">
      <span class="text-white text-lg">Your App Name</span>
    </div>
      <div>
        <button class="text-white mx-2">Products</button>
        <button class="text-white mx-2">Registration</button>
        <button class="text-white mx-2">License Activation</button>
        <button @click="logout" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">
          Sign out
        </button>
      </div>
    </nav>
  </template>
  
  <script>
  import { useAuthStore } from '../store';
  
  export default {
    name: 'Navbar',
    methods: {
      logout() {
        const store = useAuthStore();
        store.logout();
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add your component's style here */
  </style>
  