import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

interface SentimentResult {
  model: string;
  sentiment: string;
  score: number;
}

@Component({
  selector: 'app-sentiment-analysis',
  templateUrl: './sentiment-analysis.component.html',
  styleUrls: ['./sentiment-analysis.component.scss']
})
export class SentimentAnalysisComponent {
  input = '';
  selectedModels: string[] = [];
  availableModels = [
    { value: 'bert', name: 'BERT' },
    { value: 'roberta', name: 'RoBERTa' },
    { value: 'distilbert', name: 'DistilBERT' }
  ];
  results: SentimentResult[] = [];
  isLoading = false;

  constructor(private apiService: ApiService) {}

  async analyzeText() {
    if (!this.input.trim() || this.selectedModels.length === 0) return;

    this.isLoading = true;
    this.results = [];

    try {
      for (const model of this.selectedModels) {
        const result = await this.apiService.analyzeSentiment(this.input, model);
        this.results.push({
          model: this.availableModels.find(m => m.value === model)?.name || model,
          sentiment: result.sentiment,
          score: result.score
        });
      }
    } catch (error) {
      console.error('Error analyzing sentiment:', error);
    } finally {
      this.isLoading = false;
    }
  }

  getSentimentColor(sentiment: string): string {
    switch (sentiment.toLowerCase()) {
      case 'positive': return 'green';
      case 'negative': return 'red';
      case 'neutral': return 'blue';
      default: return 'gray';
    }
  }
}