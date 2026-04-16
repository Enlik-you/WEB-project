import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { PreferencesComponent } from './pages/preferences/preferences.component';
import { ResultsComponent } from './pages/results/results.component';
import { CountryDetailComponent } from './pages/country-detail/country-detail.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'preferences', component: PreferencesComponent },
  { path: 'results', component: ResultsComponent },
  { path: 'countries/:id', component: CountryDetailComponent }
];