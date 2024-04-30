import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';

// add this
import './index.css' 

const app = createApp(App);

app.use(router);
app.use(createPinia()); // Make sure Pinia is used before mounting the app

app.mount('#app');



// createApp(App).use(router).mount('#app')
