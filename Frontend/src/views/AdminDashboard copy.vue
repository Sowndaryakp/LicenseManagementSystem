<template>
  <div>
    <Navbar />
    <div class="container mx-auto mt-8">
      <h1 class="text-3xl font-bold mb-4">Admin Dashboard</h1>
      <div class="flex justify-between">
        <div class="w-1/2">
          <h2 class="text-xl font-bold mb-2">Welcome, {{ userEmail }}</h2>
          <p>This is your public dashboard.</p>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { useAuthStore } from '../store';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default defineComponent({
  name: 'PublicDashboard',
  components: {
    Navbar,
    Footer
  },
  setup() {
    const store = useAuthStore();

    return {
      userEmail: store.user ? store.user.email : '',
    };
  }
});
</script>

<style scoped>
/* Add your component's style here */
</style>
