<template>
  <div>
    <!-- Sidebar -->
    <div
      class="fixed left-0 top-0 w-64 h-full bg-deep-cerulean-700 text-white transition duration-300 ease-in-out transform"
      :class="{ '-translate-x-full': !isOpen }"
    >
      <!-- Sidebar content -->
      <div class="p-4">
        <div class="flex items-center ml-11">
          <img src="../assets/cmti.png" alt="Logo" class="h-8 mr-8">
        </div>
        <!-- Example links -->
        <ul class="mt-4">
          <li>
            <a href="#" class="block text-gray-300 hover:text-white">Example 1</a>
            <ul class="ml-4">
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 1</a></li>
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 2</a></li>
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 3</a></li>
            </ul>
          </li>
          <li>
            <a href="#" class="block text-gray-300 hover:text-white">Example 2</a>
            <ul class="ml-4">
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 1</a></li>
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 2</a></li>
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 3</a></li>
            </ul>
          </li>
          <li>
            <a href="#" class="block text-gray-300 hover:text-white">Example 3</a>
            <ul class="ml-4">
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 1</a></li>
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 2</a></li>
              <li><a href="#" class="block text-gray-300 hover:text-white">Sub Example 3</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>

    <!-- Navbar -->
    <Navbar />

    <div class="container mx-auto mt-8">
      <!-- Hamburger button -->
      <button
        class="fixed left-4 top-3 z-10 w-10 h-10 bg-deep-cerulean-700 text-white rounded-full flex items-center justify-center focus:outline-none"
        @click="toggleSidebar"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16m-7 6h7"
          ></path>
        </svg>
      </button>

      <!-- Admin Dashboard content -->
      <div class="mt-8 flex flex-col items-center">
        <h1 class="text-3xl font-bold mb-4">Admin Dashboard</h1>
        <div class="w-full max-w-md ">
          <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col items-center">
            <h2 class="text-xl font-bold mb-2">Welcome, {{ userEmail }}</h2>
            <p>This is your admin dashboard.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useAuthStore } from '../store';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default defineComponent({
  name: 'AdminDashboard',
  components: {
    Navbar,
    Footer
  },
  setup() {
    const store = useAuthStore();
    const isOpen = ref(false);

    const toggleSidebar = () => {
      isOpen.value = !isOpen.value;
    };

    return {
      userEmail: store.user ? store.user.email : '',
      isOpen,
      toggleSidebar
    };
  }
});
</script>

<style scoped>
/* Add your component's style here */
</style>
