import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { FooterComponent } from '../../components/footer/footer.component';

@Component({
  selector: 'app-preferences',
  imports: [FormsModule, NavbarComponent, FooterComponent],
  templateUrl: './preferences.component.html',
  styleUrl: './preferences.component.css'
})
export class PreferencesComponent {
  preference = {
    originCountry: '',
    monthlyBudget: 1500,
    knowsEnglish: false,
    familyStatus: 'single',
    childrenCount: 0,
    preferredClimate: 'mild',
    wantsLowCost: false,
    wantsHighSafety: true,
    wantsGoodHealthcare: true,
    wantsGoodEducation: false,
    wantsStrongJobMarket: true,
    wantsPoliticalStability: true,
    wantsFamilyFriendlyCountry: false
  };

  constructor(private router: Router) {}

  onSubmit() {
    console.log('Preferences:', this.preference);
    this.router.navigate(['/results']);
  }
}