import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { TextGenerationComponent } from './components/text-generation/text-generation.component';
import { SentimentAnalysisComponent } from './components/sentiment-analysis/sentiment-analysis.component';
import { NerVisualizationComponent } from './components/ner-visualization/ner-visualization.component';
import { UserFeedbackComponent } from './components/user-feedback/user-feedback.component';
import { PerformanceDashboardComponent } from './components/performance-dashboard/performance-dashboard.component';

import { ApiService } from './services/api.service';

const routes: Routes = [
  { path: '', redirectTo: '/text-generation', pathMatch: 'full' },
  { path: 'text-generation', component: TextGenerationComponent },
  { path: 'sentiment-analysis', component: SentimentAnalysisComponent },
  { path: 'ner-visualization', component: NerVisualizationComponent },
  { path: 'user-feedback', component: UserFeedbackComponent },
  { path: 'performance-dashboard', component: PerformanceDashboardComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    TextGenerationComponent,
    SentimentAnalysisComponent,
    NerVisualizationComponent,
    UserFeedbackComponent,
    PerformanceDashboardComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }