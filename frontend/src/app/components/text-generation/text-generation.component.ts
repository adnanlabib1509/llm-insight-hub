import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-text-generation',
  templateUrl: './text-generation.component.html',
  styleUrls: ['./text-generation.component.scss']
})
export class TextGenerationComponent {
  input = '';
  model = 'gpt2';
  output = '';
  isLoading = false;

  constructor(private apiService: ApiService) {}

  async onSubmit() {
    if (!this.input.trim()) return;

    this.isLoading = true;
    try {
      const result = await this.apiService.generateText(this.input, this.model);
      this.output = result.generated_text;
    } catch (error) {
      console.error('Error generating text:', error);
      this.output = 'An error occurred while generating text.';
    } finally {
      this.isLoading = false;
    }
  }
}