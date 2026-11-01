export const fiveFactors = [
  {
    id: "tao",
    order: "01",
    han: "道",
    vi: "Đạo",
    en: "Alignment",
    question: "Điều gì đáng làm — và vì sao?",
    description: "Kết nối vấn đề thật, giá trị cho người dùng, động lực và những điều chủ động không làm.",
    skills: ["why-strategic-rationale", "problem-discovery", "research-question"]
  },
  {
    id: "heaven",
    order: "02",
    han: "天",
    vi: "Thiên",
    en: "Conditions",
    question: "Thời điểm và ngoại cảnh đang nói gì?",
    description: "Quan sát tín hiệu có ngày tháng, cửa sổ cơ hội, hệ sinh thái và các phụ thuộc ngoài tầm kiểm soát.",
    skills: ["research-watch", "diffusion-release-tracking", "publication-strategy"]
  },
  {
    id: "earth",
    order: "03",
    han: "地",
    vi: "Địa",
    en: "Terrain",
    question: "Địa hình nào quyết định chi phí?",
    description: "Đọc ranh giới kiến trúc, dữ liệu, hệ thống cũ, năng lực đội ngũ và đường lui trước khi cam kết.",
    skills: ["c4-model", "ddd-core", "evolutionary-architecture"]
  },
  {
    id: "command",
    order: "04",
    han: "將",
    vi: "Tướng",
    en: "Leadership",
    question: "Ai chịu trách nhiệm cho kết quả?",
    description: "Làm rõ quyền quyết định, năng lực, trách nhiệm, cách giải quyết xung đột và giới hạn thẩm quyền.",
    skills: ["business-product-leadership", "agent-expertise-protocol", "architecture-decision-records"]
  },
  {
    id: "method",
    order: "05",
    han: "法",
    vi: "Pháp",
    en: "Method",
    question: "Ta học và vận hành bằng cách nào?",
    description: "Thiết kế nhịp giao hàng, kiểm thử, quan sát, bảo mật và vòng phản hồi đủ nhanh để thích nghi.",
    skills: ["dora-core", "code-quality-gate", "experiment-tracking"]
  }
];

export const pursuits = [
  {
    id: "evidence-first-research",
    status: "Deepening",
    title: "Evidence-first research systems",
    summary: "Biến câu hỏi nghiên cứu thành chuỗi bằng chứng có thể truy vết, tái lập và bảo vệ trước phản biện.",
    now: "Kết nối research question, SOTA survey, experiment tracking và paper audit thành một vòng khép kín.",
    factors: ["tao", "method"],
    skills: ["research-question", "sota-survey", "research-design", "experiment-tracking", "paper-audit"]
  },
  {
    id: "evolutionary-systems",
    status: "Deepening",
    title: "Architectures that can evolve",
    summary: "Dùng domain boundaries, decision records và fitness functions để thay đổi hệ thống có chủ đích.",
    now: "Giữ C4, DDD và Clean Architecture sát với quyết định vận hành thay vì biến thành tài liệu tĩnh.",
    factors: ["earth", "method"],
    skills: ["ddd-core", "c4-model", "clean-architecture", "evolutionary-architecture"]
  },
  {
    id: "human-authority",
    status: "Building",
    title: "Human authority in agentic work",
    summary: "Xây agent hữu ích nhưng không tự mở rộng quyền, tự nhận độ chắc chắn hoặc thay người dùng quyết định.",
    now: "Chuẩn hóa handoff, bằng chứng, escalation và ranh giới giữa thao tác local với hành động hệ quả bên ngoài.",
    factors: ["command", "method"],
    skills: ["agent-expertise-protocol", "collaborative-engineering-agent", "kinhluan-router"]
  },
  {
    id: "secure-delivery",
    status: "Building",
    title: "Secure-by-construction delivery",
    summary: "Đưa threat modeling, quality gates và remediation vào dòng giao hàng thay vì kiểm tra ở cuối.",
    now: "Nối rủi ro API, cloud, container và supply chain với kiểm thử có giới hạn, được ủy quyền rõ ràng.",
    factors: ["earth", "method"],
    skills: ["threat-modeling", "api-security", "container-security", "security-analysis"]
  },
  {
    id: "technical-vietnamese",
    status: "Sustaining",
    title: "Vietnamese technical language",
    summary: "Giữ thuật ngữ chính xác, câu văn tự nhiên và khả năng giải thích tư duy máy tính bằng tiếng Việt.",
    now: "Xây cầu nối giữa technical English, thuật ngữ tiếng Việt và cách viết học thuật có thể kiểm chứng.",
    factors: ["tao", "command"],
    skills: ["technical-english-cs", "vietnamese-cs-terminology", "vietnamese-writing-standard"]
  }
];

export const learningPaths = [
  {
    id: "research-that-holds-up",
    number: "Path 01",
    title: "Research that holds up",
    outcome: "Đi từ khoảng trống nghiên cứu đến một tuyên bố có bằng chứng, mã nguồn và đường kiểm toán rõ ràng.",
    steps: [
      "research-question",
      "sota-survey",
      "research-design",
      "experiment-tracking",
      "paper-writing",
      "internal-critique",
      "publication-strategy"
    ]
  },
  {
    id: "architecture-with-boundaries",
    number: "Path 02",
    title: "Architecture with boundaries",
    outcome: "Chuyển WHY thành ranh giới domain, kiến trúc có thể diễn giải và quyết định có thể đảo ngược.",
    steps: [
      "why-strategic-rationale",
      "ddd-core",
      "c4-model",
      "clean-architecture",
      "architecture-decision-records",
      "evolutionary-architecture"
    ]
  },
  {
    id: "ship-with-confidence",
    number: "Path 03",
    title: "Ship with confidence",
    outcome: "Tạo dòng giao hàng nhỏ, có kiểm chứng, review theo rủi ro và đo được khả năng phục hồi.",
    steps: [
      "collaborative-engineering-agent",
      "git-workflow",
      "code-quality-gate",
      "merge-request-review",
      "dora-core"
    ]
  },
  {
    id: "product-with-evidence",
    number: "Path 04",
    title: "Product with evidence",
    outcome: "Tách tín hiệu thị trường khỏi niềm tin nội bộ và chọn đúng thử nghiệm trước khi đầu tư lớn.",
    steps: [
      "problem-discovery",
      "why-strategic-rationale",
      "business-product-leadership",
      "product-ux-research",
      "product-analytics",
      "diffusion-release-tracking"
    ]
  },
  {
    id: "secure-the-system",
    number: "Path 05",
    title: "Secure the system",
    outcome: "Từ threat model đến hardening và kiểm chứng được ủy quyền, với remediation là đầu ra chính.",
    steps: [
      "threat-modeling",
      "api-security",
      "cloud-security",
      "container-security",
      "security-analysis",
      "penetration-testing"
    ]
  }
];

export const principles = [
  {
    number: "I",
    title: "Evidence before certainty",
    text: "Tách dữ kiện, suy luận và giả định. Mức tự tin phải đi sau chất lượng bằng chứng."
  },
  {
    number: "II",
    title: "Authority stays with people",
    text: "Agent có thể đề xuất và thực thi trong phạm vi được giao; quyền mở rộng phạm vi vẫn thuộc về người dùng."
  },
  {
    number: "III",
    title: "Thresholds need a local rubric",
    text: "Không biến một con số thuận tiện thành luật phổ quát. Chi phí, khả năng đảo ngược và bối cảnh quyết định ngưỡng."
  },
  {
    number: "IV",
    title: "One source, many views",
    text: "Một nguồn nội dung có thẩm quyền; catalog, package và website là các view được sinh và kiểm tra."
  },
  {
    number: "V",
    title: "Prefer reversible movement",
    text: "Thử nghiệm nhỏ, quan sát được và có exit criteria thường tốt hơn cam kết lớn dựa trên niềm tin."
  },
  {
    number: "VI",
    title: "Language is infrastructure",
    text: "Tên gọi chính xác và diễn đạt rõ ràng làm giảm lỗi phối hợp cũng thật như test hoặc schema."
  }
];
