import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { FooterComponent } from '../../components/footer/footer.component';
import { MOCK_COUNTRIES } from '../../data/mock-countries';
import { Country } from '../../interfaces/country';

@Component({
  selector: 'app-country-detail',
  imports: [NavbarComponent, FooterComponent, RouterLink],
  templateUrl: './country-detail.component.html',
  styleUrl: './country-detail.component.css'
})
export class CountryDetailComponent {
  country?: Country;

  constructor(private route: ActivatedRoute) {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.country = MOCK_COUNTRIES.find((item) => item.id === id);
  }
}