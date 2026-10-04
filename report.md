# BÁO CÁO KẾT QUẢ LAB 16 (TRACK 2)
**Nền tảng:** Microsoft Azure
**Loại tài khoản:** Azure for Students

## 1. Kết quả Phần 1 (CPU Benchmark)
- **Triển khai máy ảo:** Đã khởi tạo thành công máy ảo tại khu vực `Japan East` (do tài khoản Sinh viên bị giới hạn không thể tạo ở East US hay Malaysia West).
- **Tốc độ xử lý:** Mô hình LightGBM chạy trên máy ảo CPU 2 nhân xử lý tập dữ liệu phát hiện gian lận thẻ tín dụng vô cùng mượt mà. Thời gian huấn luyện (Training time) chỉ mất vỏn vẹn **5.03 giây**.
- **Độ chính xác:** Mô hình đạt Accuracy cực kỳ cao: **99.82%** (AUC-ROC: 0.82). 
- **Tốc độ Inference:** Thời gian dự đoán cho 1 dòng dữ liệu cực thấp, chỉ mất **0.0017 giây**. Điều này chứng tỏ máy ảo Cloud hoàn toàn có khả năng đáp ứng tốt cho các hệ thống thời gian thực (Real-time).

## 2. Giải trình về phần Chi phí (Cost Management)
- Bức ảnh chụp Cost Management hiển thị là **$0.00 (No Cost)**. 
- Nguyên nhân: Do em có ý thức quản lý tài nguyên, chủ động dọn dẹp và xóa triệt để máy ảo (`Resource Group: ai-lab-rg-japan`) ngay lập tức sau khi test thành công. Đồng thời hệ thống Azure cần 24 giờ để cập nhật chi phí, nên số tiền phát sinh nhỏ (chưa tới 30 phút sử dụng) chưa đủ để hiển thị.

## 3. Kết quả Phần 2 (Tùy chọn: GPU & vLLM)
- Mặc định tài khoản Azure for Students bị khóa mức Quota GPU = 0.
- Em đã thực hiện các bước tạo Request để xin mở giới hạn Quota cho dòng máy `NCASv3_T4` tại Japan East. Tuy nhiên, hệ thống Azure tự động từ chối yêu cầu đối với tài khoản Sinh viên. Do đó, em xin phép bỏ qua phần bài tập nâng cao này.

---
*(Kèm theo bài báo cáo là 2 file: benchmark_result.json, cloud-init-cpu.yaml cùng các hình ảnh chụp màn hình chứng minh kết quả).*
