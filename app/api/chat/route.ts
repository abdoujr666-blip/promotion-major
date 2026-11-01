import { GoogleGenAI } from '@google/genai';
import { NextResponse } from 'next/server';

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

export async function POST(req: Request) {
  try {
    const { messages } = await req.json();
    const latestMessage = messages[messages.length - 1].content;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: latestMessage,
    });

    return NextResponse.json({ role: 'assistant', content: response.text });
  } catch (error) {
    console.error('API Error:', error);
    return NextResponse.json({ error: 'Failed to generate response' }, { status: 500 });
  }
}
