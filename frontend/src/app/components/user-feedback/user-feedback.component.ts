import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

interface FeedbackItem {
  modelType: string;
  modelName: string;
  rating: number;
  comment: string;
}

@Component({
  selector: 'app-user-feedback',
  templateUrl: './user-feedback.component.html',
  styleUrls: ['./user-feedback.component.scss']
})
export class UserFeedbackComponent {
  feedbackItem: FeedbackItem = {
    modelType: '',
    modelName: '',
    rating: 0,
    comment: ''
  };

  modelTypes = ['Text Generation', 'Sentiment Analysis', 'Named Entity Recognition'];
  modelNames: { [key: string]: string[] } = {
    'Text Generation': ['GPT-2', 'BERT', 'T5'],
    'Sentiment Analysis': ['BERT', 'RoBERTa', 'DistilBERT'],
    'Named Entity Recognition': ['spaCy', 'Flair', 'Stanford NER']
  };

  isSubmitting = false;
  feedbackSubmitted = false;

  constructor(private apiService: ApiService) {}

  onModelTypeChange() {
    this.feedbackItem.modelName = '';
  }

  async submitFeedback() {
    if (this.isFormValid()) {
      this.isSubmitting = true;
      try {
        await this.apiService.submitFeedback(this.feedbackItem);
        this.feedbackSubmitted = true;
        this.resetForm();
      } catch (error) {
        console.error('Error submitting feedback:', error);
        // Handle error (e.g., show error message to user)
      } finally {
        this.isSubmitting = false;
      }
    }
  }

  isFormValid(): boolean {
    return this.feedbackItem.modelType !== '' &&
           this.feedbackItem.modelName !== '' &&
           this.feedbackItem.rating > 0 &&
           this.feedbackItem.comment.trim() !== '';
  }

  resetForm() {
    this.feedbackItem = {
      modelType: '',
      modelName: '',
      rating: 0,
      comment: ''
    };
  }
}