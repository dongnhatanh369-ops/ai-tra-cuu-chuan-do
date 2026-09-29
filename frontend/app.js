const API_BASE_URL = window.AI_API_BASE_URL || "http://127.0.0.1:8000";

const translations = {
  vi: {
    label: "Ngôn ngữ", title: "Tra cứu tài liệu hóa học",
    subtitle: "Đặt câu hỏi về phương pháp chuẩn độ, công thức, chỉ thị hoặc quy trình thí nghiệm.",
    welcome: "Xin chào! Tôi có thể hỗ trợ tra cứu tài liệu chuẩn độ. Bạn muốn tìm hiểu điều gì?",
    question: "Câu hỏi", placeholder: "Ví dụ: Chuẩn độ HCl bằng NaOH nên dùng chỉ thị nào?",
    ready: "Sẵn sàng", send: "Gửi câu hỏi", processing: "Đang xử lý…", connection: "Có lỗi kết nối",
    notice: "Thông tin AI cần được kiểm tra với tài liệu và quy định an toàn phòng thí nghiệm.",
    backend: "Backend không thể xử lý câu hỏi.", empty: "Backend chưa trả về nội dung trả lời.", cannot: "Không thể kết nối AI"
  },
  en: {
    label: "Language", title: "Chemical Information Search",
    subtitle: "Ask about titration methods, formulas, indicators, or laboratory procedures.",
    welcome: "Hello! I can help you search titration resources. What would you like to learn?",
    question: "Question", placeholder: "Example: Which indicator should be used to titrate HCl with NaOH?",
    ready: "Ready", send: "Ask question", processing: "Processing…", connection: "Connection error",
    notice: "AI information should be checked against laboratory references and safety procedures.",
    backend: "The backend could not process the question.", empty: "The backend returned no answer.", cannot: "Could not connect to AI"
  }
};

const form = document.querySelector("#question-form");
const input = document.querySelector("#question");
const conversation = document.querySelector("#conversation");
const status = document.querySelector("#status");
const sendButton = document.querySelector("#send-button");
const languageSelect = document.querySelector("#language-select");
let language = localStorage.getItem("ai-language") || "vi";

function text(key) { return translations[language][key]; }
function applyLanguage() {
  document.documentElement.lang = language;
  document.querySelector("#language-label").textContent = text("label");
  document.querySelector("#title").textContent = text("title");
  document.querySelector("#subtitle").textContent = text("subtitle");
  document.querySelector("#welcome-message").textContent = text("welcome");
  document.querySelector("#question-label").textContent = text("question");
  input.placeholder = text("placeholder");
  status.textContent = text("ready");
  sendButton.textContent = text("send");
  document.querySelector("#notice").textContent = text("notice");
}
function addMessage(value, role) {
  const message = document.createElement("div");
  message.className = `message ${role}`;
  message.textContent = value;
  conversation.append(message);
  conversation.scrollTop = conversation.scrollHeight;
}

languageSelect.value = language;
languageSelect.addEventListener("change", () => {
  language = languageSelect.value;
  localStorage.setItem("ai-language", language);
  applyLanguage();
});
applyLanguage();

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  addMessage(question, "user");
  input.value = "";
  input.disabled = true;
  sendButton.disabled = true;
  status.textContent = text("processing");
  try {
    const response = await fetch(`${API_BASE_URL}/api/v1/ai/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, language })
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || text("backend"));
    addMessage(data.answer || text("empty"), "assistant");
    status.textContent = text("ready");
  } catch (error) {
    addMessage(`${text("cannot")}: ${error.message}`, "assistant error");
    status.textContent = text("connection");
  } finally {
    input.disabled = false;
    sendButton.disabled = false;
    input.focus();
  }
});
