import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  // Text Generation
  generateText(input: string, model: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/generate-text`, { input, model });
  }

  // Sentiment Analysis
  analyzeSentiment(input: string, model: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/analyze-sentiment`, { input, model });
  }

  // Named Entity Recognition
  performNER(input: string, model: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/perform-ner`, { input, model });
  }

  // User Feedback
  submitFeedback(feedback: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/submit-feedback`, feedback);
  }

  // Performance Dashboard
  getPerformanceData(): Observable<any> {
    return this.http.get(`${this.apiUrl}/performance-data`);
  }

  // Error handling method (optional, can be used in components)
  handleError(error: any): Promise<any> {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}