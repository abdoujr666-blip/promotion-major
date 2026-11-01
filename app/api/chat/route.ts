import { createGoogleGenerativeAI } from '@ai-sdk/google';
import { streamText } from 'ai';

const google = createGoogleGenerativeAI({
  apiKey: process.env.GEMINI_API_KEY,
});

export async function POST(req: Request) {
  const { messages } = await req.json();
  const result = streamText({
    model: google('gemini-1.5-flash'),
    messages,
  });
  return result.toDataStreamResponse();
}
