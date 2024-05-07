<template>
  <nav class="bg-deep-cerulean-700 p-4 flex justify-between items-center">
    <div class="flex items-center ml-11">
  <img src="../assets/cmti.png" alt="Logo" class="h-8 mr-8" style="filter: invert(1);"> <!-- Use filter: invert(1); to display the logo in white color -->
  <span class="text-white text-lg">Smart Metrology Workshop</span>
</div>

    <div>
      <button class="text-white mx-3">Products</button>
      <button class="text-white mx-3">Registration</button>
      <button class="text-white mx-3">License Activation</button>
      <button @click="logout" class="bg-red-500 rounded-md hover:bg-red-600 text-white font-bold py-2 px-4 rounded">
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
