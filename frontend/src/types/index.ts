export interface Activity {
  id: number;
  time: string;
  name: string;
  eventOrStore: string;
  value: string;
}

export interface Event {
  id: number;
  name: string;
  issued: number;
  remaining: number;
  revenue: string;
}
