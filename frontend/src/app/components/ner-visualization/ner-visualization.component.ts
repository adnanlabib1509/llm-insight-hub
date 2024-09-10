import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

interface Entity {
  text: string;
  type: string;
  start: number;
  end: number;
}

@Component({
  selector: 'app-ner-visualization',
  templateUrl: './ner-visualization.component.html',
  styleUrls: ['./ner-visualization.component.scss']
})
export class NerVisualizationComponent {
  input = '';
  model = 'spacy';
  availableModels = [
    { value: 'spacy', name: 'spaCy' },
    { value: 'flair', name: 'Flair' },
    { value: 'stanford', name: 'Stanford NER' }
  ];
  entities: Entity[] = [];
  isLoading = false;

  constructor(private apiService: ApiService) {}

  async visualizeNER() {
    if (!this.input.trim()) return;

    this.isLoading = true;
    this.entities = [];

    try {
      const result = await this.apiService.performNER(this.input, this.model);
      this.entities = result.entities;
    } catch (error) {
      console.error('Error performing NER:', error);
    } finally {
      this.isLoading = false;
    }
  }

  getHighlightedText(): string {
    if (this.entities.length === 0) return this.input;

    let result = '';
    let lastIndex = 0;

    for (const entity of this.entities) {
      result += this.input.slice(lastIndex, entity.start);
      result += `<span class="entity ${entity.type.toLowerCase()}" title="${entity.type}">${this.input.slice(entity.start, entity.end)}</span>`;
      lastIndex = entity.end;
    }

    result += this.input.slice(lastIndex);
    return result;
  }
}