import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { FooterComponent } from '../../components/footer/footer.component';
import { MOCK_COUNTRIES } from '../../data/mock-countries';
import { Country } from '../../interfaces/country';

@Component({
  selector: 'app-results',
  imports: [NavbarComponent, FooterComponent, RouterLink],
  templateUrl: './results.component.html',
  styleUrl: './results.component.css'
})
export class ResultsComponent {
  countries: Country[] = MOCK_COUNTRIES;
}