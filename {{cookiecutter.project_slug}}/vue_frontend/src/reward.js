import {createApp} from 'vue'
import {createPinia} from 'pinia'
import {convertDatasetToProperties, djangoPropertiesPlugin} from "@/util/create_app_utils";
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import RewardClaim from "@/components/RewardClaim.vue";
import PointsStatus from "@/components/PointsStatus.vue";

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)


const statusEl = document.getElementById('points-status')
if (statusEl) {
  const app = createApp(PointsStatus, convertDatasetToProperties({
    dataset: {...statusEl.dataset},
    component: PointsStatus
  }))
  app.use(pinia)
  app.use(djangoPropertiesPlugin, statusEl)
  app.mount(statusEl)
}

document.querySelectorAll('.reward-claim').forEach(el => {
      const app = createApp(RewardClaim, convertDatasetToProperties({
        dataset: {...el.dataset},
        component: RewardClaim
      }))
      app.use(pinia)
      app.use(djangoPropertiesPlugin, el)
      app.mount(el)
    }
);
