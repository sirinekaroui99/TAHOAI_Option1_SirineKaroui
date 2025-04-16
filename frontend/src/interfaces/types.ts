export interface ClassificationResponse {
    label: string;
    confidence: number;
  }
  
  export interface ApiError {
    detail: string;
    status_code: number;
  }
  
  export enum LoadingState {
    IDLE = 'idle',
    LOADING = 'loading',
    SUCCESS = 'success',
    ERROR = 'error'
  }