import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user: null
  }),
  actions: {
    login(email, password) {
      // Simulate login process
      if (email === 'user@example.com' && password === 'password') {
        this.isLoggedIn = true;
        this.user = { email };
        console.log('Logged in as:', email); // Log the username
      } else {
        // alert('Invalid email or password');
      }
    },
    logout() {
      this.isLoggedIn = false;
      this.user = null;
    }
  }
});
