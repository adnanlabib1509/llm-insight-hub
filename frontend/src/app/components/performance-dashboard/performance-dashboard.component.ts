import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

interface ModelPerformance {
  modelName: string;
  avgAccuracy: number;
  avgLatency: number;
  userRating: number;
}

interface PerformanceData {
  textGeneration: ModelPerformance[];
  sentimentAnalysis: ModelPerformance[];
  namedEntityRecognition: ModelPerformance[];
}

@Component({
  selector: 'app-performance-dashboard',
  templateUrl: './performance-dashboard.component.html',
  styleUrls: ['./performance-dashboard.component.scss']
})
export class PerformanceDashboardComponent implements OnInit {
  performanceData: PerformanceData = {
    textGeneration: [],
    sentimentAnalysis: [],
    namedEntityRecognition: []
  };
  isLoading = true;
  error = '';

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.fetchPerformanceData();
  }

  async fetchPerformanceData() {
    try {
      this.isLoading = true;
      this.performanceData = await this.apiService.getPerformanceData();
    } catch (error) {
      console.error('Error fetching performance data:', error);
      this.error = 'An error occurred while fetching performance data. Please try again later.';
    } finally {
      this.isLoading = false;
    }
  }

  getModelTypeData(modelType: keyof PerformanceData): ModelPerformance[] {
    return this.performanceData[modelType];
  }
}