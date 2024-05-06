import { createRouter, createWebHistory } from 'vue-router';
import AdminDashboard from '../views/AdminDashboard.vue';
import PublicDashboard from '../views/PublicDashboard.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import { useAuthStore } from '../store';

const routes = [
  {
    path: '/user',
    component: () => import('../App.vue'),
    children: [
      {
        path: 'Login',
        name: 'Login',
        component: Login
      },
      {
        path: 'register', 
        name: 'Register',
        component: Register
      }
    ]
  },
  {
    path: '/admindashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true, isAdmin: true }
  },
  {
    path: '/publicdashboard',
    name: 'PublicDashboard',
    component: PublicDashboard,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const store = useAuthStore();
  const isLoggedIn = store.isLoggedIn;
  const isAdmin = store.user && store.user.email === 'sow@gmail.com';

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      next({ name: 'Login' });
    } else {
      if (to.matched.some(record => record.meta.isAdmin)) {
        if (!isAdmin) {
          next({ name: 'PublicDashboard' });
        } else {
          next();
        }
      } else {
        next();
      }
    }
  } else {
    next();
  }
});

export default router;
